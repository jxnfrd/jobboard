import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobsp.settings")
django.setup()

from peeldb.models import User

def activate_users():
    updated = User.objects.filter(is_active=False).update(is_active=True)
    print(f"Activated {updated} users.")
    
    # Also ensure superusers have is_staff=True
    staff_updated = User.objects.filter(is_superuser=True, is_staff=False).update(is_staff=True)
    print(f"Set is_staff=True for {staff_updated} superusers.")

if __name__ == "__main__":
    activate_users()
