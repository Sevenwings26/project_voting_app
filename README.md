
# Voting App

## Overview
My level 2 - python project.
This is voting app facilitates the registration of voters, commencement of elections, and voter verification. The application consists of three main scripts:

1. **start_registration.py**: Used for registering voters.
2. **start_election.py**: Commences the election.
3. **voter_verification.py**: Verifies if a voter is eligible to vote based on the voter identification number.

Before deploying the program, it is crucial to set up a local database and establish the necessary connections. Please follow the instructions below to configure the database connection.

## Database Setup

1. **Create a Database:**
   - Set up a local database using your preferred database management system (e.g., MySQL, PostgreSQL).

2. **Configure Connection:**
   - Open the `config.py` file.
   - Update the database connection parameters (e.g., host, user, password) to match your local database configuration.

## Usage

### 1. Voter Registration

To register voters, execute the following command:

```bash
python start_registration.py
```

This script will prompt you to enter voter information and store it in the database.

### 2. Election Commencement

To commence the election, use the following command:

```bash
python start_election.py
```

This script initializes the election process and allows eligible voters to cast their votes.

### 3. Voter Verification

The `voter_verification.py` script verifies whether a voter is eligible to vote. Execute the following command:

```bash
python voter_verification.py
```

The script will prompt you to enter the voter identification number and check it against the database to determine eligibility.

## Important Note

Ensure that you have set up the database connection in the `config.py` file before running any of the scripts.

## Contributing

Feel free to contribute to the improvement of this voting app by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
