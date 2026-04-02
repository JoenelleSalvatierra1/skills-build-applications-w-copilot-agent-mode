from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name="Marvel", description="Marvel superheroes team")
        dc = Team.objects.create(name="DC", description="DC superheroes team")

        # Create Users
        users = [
            User.objects.create(name="Tony Stark", email="tony@marvel.com", team=marvel.name),
            User.objects.create(name="Steve Rogers", email="steve@marvel.com", team=marvel.name),
            User.objects.create(name="Bruce Wayne", email="bruce@dc.com", team=dc.name),
            User.objects.create(name="Clark Kent", email="clark@dc.com", team=dc.name),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type="Running", duration=30, date="2024-01-01")
        Activity.objects.create(user=users[1], activity_type="Cycling", duration=45, date="2024-01-02")
        Activity.objects.create(user=users[2], activity_type="Swimming", duration=60, date="2024-01-03")
        Activity.objects.create(user=users[3], activity_type="Yoga", duration=20, date="2024-01-04")

        # Create Workouts
        Workout.objects.create(name="Pushups", description="Upper body strength", difficulty="Easy")
        Workout.objects.create(name="Squats", description="Lower body strength", difficulty="Medium")
        Workout.objects.create(name="Plank", description="Core strength", difficulty="Hard")

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], points=100, rank=1)
        Leaderboard.objects.create(user=users[1], points=90, rank=2)
        Leaderboard.objects.create(user=users[2], points=80, rank=3)
        Leaderboard.objects.create(user=users[3], points=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
