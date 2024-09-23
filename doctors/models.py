from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()  # Daily work hours start time
    end_time = models.TimeField()    # Daily work hours end time

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"Appointment with {self.doctor.name} from {self.start_datetime} to {self.end_datetime}"

    class Meta:
        # Ensures no overlapping appointments for a doctor
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'start_datetime', 'end_datetime'],
                name='unique_appointment'
            )
        ]
