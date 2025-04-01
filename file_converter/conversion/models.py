from django.db import models

class FileDownload(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    FORMAT_CHOICES = [
        ('mp3', 'MP3'),
        ('wav', 'WAV'),
        ('aac', 'AAC')
    ]

    video_url = models.URLField()
    title = models.CharField(max_length=255, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)  # En segundos
    file_size = models.PositiveIntegerField(blank=True, null=True) # En Bytes
    audio_file = models.FileField(upload_to='downloads/', blank=True, null=True)
    temp_file_path = models.CharField(max_length=255, blank=True, null=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default='mp3')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_status(self, new_status):
        """Actualiza el estado de la descarga."""
        self.status = new_status
        self.save()

    def __str__(self):
        return f"{self.title or 'Unknown'} ({self.status})"

