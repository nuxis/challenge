from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random

from core.models import Config, UserProfile
from levels.models import Level, Attempt, Score


class Command(BaseCommand):
    help = "Seed the database with test data for the challenge platform"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Remove existing test data before seeding",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Provide detailed output during seeding",
        )

    def handle(self, *args, **options):
        if options["flush"]:
            self.flush_data()

        self.create_config()
        self.create_users()
        self.create_levels()
        self.create_attempts_and_scores()

        self.stdout.write(self.style.SUCCESS("Test data seeded successfully!"))

    def flush_data(self):
        """Remove existing test data"""
        self.stdout.write("Flushing existing test data...")
        Attempt.objects.all().delete()
        Score.objects.all().delete()
        Level.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().filter(is_staff=False).delete()
        Config.objects.all().delete()
        self.stdout.write("Test data flushed.")

    def create_config(self):
        """Create site configuration"""
        if Config.objects.exists():
            self.stdout.write("Config already exists, skipping...")
            return

        config = Config.objects.create(
            eventname="Test Challenge 2024",
            welcometext="Welcome to the test challenge! This is a sample event for testing purposes.",
            active=True,
            webhook_admins=None,
        )
        self.stdout.write(f"Created config: {config.eventname}")

    def create_users(self):
        """Create test users with various roles"""
        users_data = [
            # Admin users
            {
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "is_staff": True,
            },
            {
                "username": "moderator",
                "email": "mod@example.com",
                "first_name": "Mod",
                "last_name": "User",
                "is_staff": True,
            },
            # Power users (high scores)
            {
                "username": "alice",
                "email": "alice@example.com",
                "first_name": "Alice",
                "last_name": "Smith",
            },
            {
                "username": "bob",
                "email": "bob@example.com",
                "first_name": "Bob",
                "last_name": "Johnson",
            },
            {
                "username": "charlie",
                "email": "charlie@example.com",
                "first_name": "Charlie",
                "last_name": "Brown",
            },
            # Regular users
            {
                "username": "diana",
                "email": "diana@example.com",
                "first_name": "Diana",
                "last_name": "Prince",
            },
            {
                "username": "eve",
                "email": "eve@example.com",
                "first_name": "Eve",
                "last_name": "Wilson",
            },
            {
                "username": "frank",
                "email": "frank@example.com",
                "first_name": "Frank",
                "last_name": "Miller",
            },
            {
                "username": "grace",
                "email": "grace@example.com",
                "first_name": "Grace",
                "last_name": "Lee",
            },
            {
                "username": "henry",
                "email": "henry@example.com",
                "first_name": "Henry",
                "last_name": "Davis",
            },
            # Casual users (low activity)
            {
                "username": "iris",
                "email": "iris@example.com",
                "first_name": "Iris",
                "last_name": "Garcia",
            },
            {
                "username": "jack",
                "email": "jack@example.com",
                "first_name": "Jack",
                "last_name": "Martinez",
            },
            {
                "username": "kate",
                "email": "kate@example.com",
                "first_name": "Kate",
                "last_name": "Anderson",
            },
            {
                "username": "leo",
                "email": "leo@example.com",
                "first_name": "Leo",
                "last_name": "Taylor",
            },
            # Inactive users (no attempts)
            {
                "username": "maya",
                "email": "maya@example.com",
                "first_name": "Maya",
                "last_name": "Thomas",
            },
            {
                "username": "noah",
                "email": "noah@example.com",
                "first_name": "Noah",
                "last_name": "White",
            },
            {
                "username": "olivia",
                "email": "olivia@example.com",
                "first_name": "Olivia",
                "last_name": "Harris",
            },
        ]

        for user_data in users_data:
            if not User.objects.filter(username=user_data["username"]).exists():
                user = User.objects.create_user(
                    username=user_data["username"],
                    email=user_data["email"],
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    password="password123",  # Same password for all test users
                    is_staff=user_data.get("is_staff", False),
                )
                self.stdout.write(f"Created user: {user.username}")

    def create_levels(self):
        """Create challenge levels with varying difficulty"""
        levels_data = [
            {
                "name": "Welcome",
                "description": "Get started with this simple challenge",
                "points": 10,
                "question": "What is 2 + 2?",
                "answer": "4",
                "required_points": 0,
                "required_attempts": 0,
                "is_external": False,
                "multianswer": False,
            },
            {
                "name": "Basic Math",
                "description": "Test your arithmetic skills",
                "points": 15,
                "question": "What is 15 × 4?",
                "answer": "60",
                "required_points": 10,
                "required_attempts": 0,
                "is_external": False,
                "multianswer": False,
            },
            {
                "name": "Flag Hunt",
                "description": "Find the hidden flag",
                "points": 20,
                "question": "The flag is hidden in this level. Try some common flag formats!",
                "answer": "FLAG{hidden_treasure}",
                "required_points": 25,
                "required_attempts": 0,
                "is_external": False,
                "multianswer": False,
            },
            {
                "name": "Multiple Choice",
                "description": "This level accepts multiple answers",
                "points": 25,
                "question": "Name a primary color",
                "answer": "RED||BLUE||YELLOW",
                "required_points": 45,
                "required_attempts": 2,
                "is_external": False,
                "multianswer": True,
            },
            {
                "name": "Web Challenge",
                "description": "External challenge level",
                "points": 30,
                "question": "This challenge is verified externally. Submit any answer to test the connection.",
                "answer": "https://httpbin.org/status/200",
                "required_points": 70,
                "required_attempts": 0,
                "is_external": True,
                "multianswer": False,
            },
            {
                "name": "Crypto Basics",
                "description": "Basic cryptography challenge",
                "points": 35,
                "question": "Decode this Caesar cipher: FRZDUGV",
                "answer": "CRYPTIC",
                "required_points": 100,
                "required_attempts": 3,
                "is_external": False,
                "multianswer": False,
            },
            {
                "name": "Logic Puzzle",
                "description": "Test your logical thinking",
                "points": 40,
                "question": "If A=1, B=2, C=3, what does 8-5-12-12-15 equal?",
                "answer": "HELLO",
                "required_points": 135,
                "required_attempts": 0,
                "is_external": False,
                "multianswer": False,
            },
            {
                "name": "Final Challenge",
                "description": "The ultimate test",
                "points": 50,
                "question": "What is the answer to life, the universe, and everything?",
                "answer": "42",
                "required_points": 175,
                "required_attempts": 5,
                "is_external": False,
                "multianswer": False,
            },
        ]

        for level_data in levels_data:
            if not Level.objects.filter(name=level_data["name"]).exists():
                level = Level.objects.create(**level_data)
                self.stdout.write(
                    f"Created level: {level.name} ({level.points} points)"
                )

    def create_attempts_and_scores(self):
        """Create realistic attempt patterns and scores"""
        users = list(User.objects.filter(is_staff=False))
        levels = list(Level.objects.all().order_by("required_points"))

        if not users or not levels:
            self.stdout.write("No users or levels found, skipping attempts creation")
            return

        # User completion patterns
        completion_patterns = {
            "alice": 1.0,  # 100% completion (power user)
            "bob": 1.0,  # 100% completion (power user)
            "charlie": 0.875,  # 87.5% completion (power user)
            "diana": 0.75,  # 75% completion (regular user)
            "eve": 0.625,  # 62.5% completion (regular user)
            "frank": 0.5,  # 50% completion (regular user)
            "grace": 0.375,  # 37.5% completion (casual user)
            "henry": 0.25,  # 25% completion (casual user)
            "iris": 0.125,  # 12.5% completion (casual user)
            "jack": 0.125,  # 12.5% completion (casual user)
            "kate": 0.0,  # 0% completion (inactive)
            "leo": 0.0,  # 0% completion (inactive)
            "maya": 0.0,  # 0% completion (inactive)
            "noah": 0.0,  # 0% completion (inactive)
            "olivia": 0.0,  # 0% completion (inactive)
        }

        for user in users:
            completion_rate = completion_patterns.get(user.username, 0.5)
            levels_to_attempt = levels[: int(len(levels) * completion_rate)]

            for i, level in enumerate(levels_to_attempt):
                # Calculate time for attempts (more recent for recent levels)
                days_ago = (len(levels_to_attempt) - i) * 2
                base_time = timezone.now() - timedelta(days=days_ago)

                # Create attempts with wrong answers before success
                wrong_answers = [
                    "wrong",
                    "incorrect",
                    "try again",
                    "not this",
                    "maybe",
                    "test",
                    "hello",
                ]
                num_wrong_attempts = random.randint(0, min(3, level.required_attempts))

                for j in range(num_wrong_attempts):
                    attempt_time = base_time - timedelta(minutes=j * 10)
                    Attempt.objects.create(
                        user=user,
                        level=level,
                        answer=random.choice(wrong_answers),
                        correct=False,
                        time=attempt_time,
                    )

                # Create successful attempt
                if (
                    not level.is_external or random.random() > 0.3
                ):  # 70% success rate for external levels
                    success_time = base_time + timedelta(minutes=5)
                    Attempt.objects.create(
                        user=user,
                        level=level,
                        answer=level.answer,
                        correct=True,
                        time=success_time,
                    )

                    # Create corresponding score and update level completion
                    Score.objects.create(
                        user=user,
                        level=level,
                        points=level.points,
                        awarded=success_time,
                    )

                    # Update level completion count
                    level.completed += 1
                    level.save()

                    # Create corresponding score and update level completion
                    Score.objects.create(
                        user=user,
                        level=level,
                        points=level.points,
                        awarded=success_time,
                    )

                    # Update level completion count
                    level.completed += 1
                    level.save()

        self.stdout.write("Created attempts and scores for all users")
