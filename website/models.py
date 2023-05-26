from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def encrypt(self, text, shift):
        encrypted_text = ''
        for char in text:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def save(self, *args, **kwargs):
        # Encrypt the fields before saving
        shift = 3  # Shift value for the Caesar cipher
        self.name = self.encrypt(self.name, shift)
        self.email = self.encrypt(self.email, shift)
        self.address = self.encrypt(self.address, shift)
        super().save(*args, **kwargs)

