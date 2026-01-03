# Test Data Seeding

The test data and the management command for seeding it is created by some AI. It seems to work for now.

This document explains how to use the test data seeding functionality for the challenge platform.

## Usage

The `seed_data` management command creates realistic test data for the challenge platform including users, levels, attempts, and scores.

### Basic Usage

```bash
python manage.py seed_data
```

### Options

- `--flush`: Remove existing test data before seeding new data
- `--verbose`: Provide detailed output during the seeding process

```bash
# Remove all existing test data and create fresh data
python manage.py seed_data --flush --verbose
```

## What Gets Created

### Users (17 total)
- **Admin users (2)**: `admin`, `moderator` - Staff accounts with elevated privileges
- **Power users (3)**: `alice`, `bob`, `charlie` - Users with 100%, 100%, and 87.5% completion rates
- **Regular users (5)**: `diana`, `eve`, `frank`, `grace`, `henry` - Users with varying completion rates (75%-25%)
- **Casual users (3)**: `iris`, `jack`, `kate` - Users with low activity (12.5% completion)
- **Inactive users (4)**: `maya`, `noah`, `olivia`, `leo` - Users with no attempts

All users have the password: `password123`

### Levels (8 total)

| Name | Points | Required Points | Features |
|------|--------|----------------|----------|
| Welcome | 10 | 0 | Simple arithmetic |
| Basic Math | 15 | 10 | Arithmetic challenge |
| Flag Hunt | 20 | 25 | CTF-style flag finding |
| Multiple Choice | 25 | 45 | Multiple correct answers |
| Web Challenge | 30 | 70 | External validation |
| Crypto Basics | 35 | 100 | Caesar cipher |
| Logic Puzzle | 40 | 135 | Letter-to-number mapping |
| Final Challenge | 50 | 175 | Ultimate challenge |

### Attempts and Scores
- **64 attempts** total across all users
- **43 scores** (successful completions)
- Realistic attempt patterns with wrong answers before success
- Proper timing to show progression over days

### Site Configuration
- Event name: "Test Challenge 2024"
- Welcome text with instructions
- Active status enabled

## Test Scenarios

The created data supports various testing scenarios:

1. **Leaderboard Testing**: Users with different scores and rankings
2. **Level Progression**: Users at different completion stages
3. **Permission Testing**: Admin vs regular user access
4. **Performance Testing**: Multiple users and attempts
5. **External Integration**: Web challenge level with HTTP callback

## Idempotent Behavior

By default, the command is idempotent - it won't create duplicate data. Use `--flush` to remove all existing test data and start fresh.

## Notes

- External challenges use `httpbin.org/status/200` for testing
- All times are realistic with proper timezone handling
- User profiles are automatically created with Django signals
- Score updates trigger the built-in webhook functionality (if configured)
