import os
from django.shortcuts import render
from django.http import JsonResponse, FileResponse, Http404
from .models import FileDownload
import yt_dlp

class DeleteOnCloseFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'rb')
    
    def read(self, *args, **kwargs):
        return self.file.read(*args, **kwargs)
    
    def close(self):
        try:
            self.file.close()
        finally:
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
    
    def __getattr__(self, attr):
        return getattr(self.file, attr)

def youtube_converter(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')

        if not video_url:
            return JsonResponse({'error': 'No video URL provided'}, status=400)
        
        file_download = FileDownload.objects.create(video_url=video_url)

        try:
            file_download.update_status('in_progress')

            # Descargar y convertir el video a MP3 
            output_data = download_audio_with_ytdlp(video_url)
            
            # Actualizar los campos del modelo con la información obtenida
            file_download.title = output_data.get('title')
            file_download.duration = output_data.get('duration')
            file_download.file_size = output_data.get('file_size')
            file_download.temp_file_path = output_data.get('output_path')
            file_download.audio_file.name = output_data.get('output_path')
            file_download.update_status('completed')
            file_download.save()
        
        except Exception as e:
            file_download.error_message = str(e)
            file_download.update_status('failed')
            file_download.save()
        
        return render(request, 'conversion/status.html', {'file_download': file_download})

    return render(request, 'conversion/youtube_converter.html')

def download_audio_with_ytdlp(video_url):
    """Descarga el audio de un video de YouTube usando yt-dlp."""
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(video_url, download=True)
        output_path = ydl.prepare_filename(info).replace('.webm', '.mp3')  
        title = info.get('title')
        duration = info.get('duration')
        file_size = info.get('filesize') or info.get('filesize_approx')
        return {
            'output_path': output_path,
            'title': title,
            'duration': duration,
            'file_size': file_size,
        }   

def download_file(request, download_id):
    try:
        file_download = FileDownload.objects.get(pk=download_id)
        file_path = file_download.temp_file_path

        if not file_path or not os.path.exists(file_path):
            raise Http404("El archivo no se encontró en el servidor")

        # Abrir el archivo y mantenerlo abierto durante la respuesta
        file_handle = DeleteOnCloseFile(file_path)

        response = FileResponse(file_handle, content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response

    except FileDownload.DoesNotExist:
        raise Http404("Registro no encontrado")
    except Exception as e:
        # Loguear el error para diagnóstico
        print(f"Error al procesar la descarga: {e}")
        raise Http404("Se produjo un error al procesar la descarga")
    
