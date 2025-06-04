
# This script uses PyMongo to insert test data directly into MongoDB.
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data using PyMongo.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Users
        users = [
            { 'email': 'alice@example.com', 'name': 'Alice', 'password': 'alicepass' },
            { 'email': 'bob@example.com', 'name': 'Bob', 'password': 'bobpass' },
            { 'email': 'carol@example.com', 'name': 'Carol', 'password': 'carolpass' }
        ]
        db.users.delete_many({})
        db.users.insert_many(users)

        # Teams
        teams = [
            { 'name': 'Team Alpha', 'members': ['alice@example.com', 'bob@example.com'] },
            { 'name': 'Team Beta', 'members': ['carol@example.com'] }
        ]
        db.teams.delete_many({})
        db.teams.insert_many(teams)

        # Activities
        activities = [
            { 'user': 'alice@example.com', 'activity_type': 'run', 'duration': 30, 'date': datetime.utcnow() },
            { 'user': 'bob@example.com', 'activity_type': 'walk', 'duration': 45, 'date': datetime.utcnow() },
            { 'user': 'carol@example.com', 'activity_type': 'strength', 'duration': 60, 'date': datetime.utcnow() }
        ]
        db.activity.delete_many({})
        db.activity.insert_many(activities)

        # Leaderboard
        leaderboard = [
            { 'team': 'Team Alpha', 'points': 150 },
            { 'team': 'Team Beta', 'points': 100 }
        ]
        db.leaderboard.delete_many({})
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            { 'user': 'alice@example.com', 'workout_type': 'cardio', 'details': '30 min run', 'date': datetime.utcnow() },
            { 'user': 'bob@example.com', 'workout_type': 'walk', 'details': '45 min walk', 'date': datetime.utcnow() },
            { 'user': 'carol@example.com', 'workout_type': 'strength', 'details': '60 min strength', 'date': datetime.utcnow() }
        ]
        db.workouts.delete_many({})
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully using PyMongo.'))
