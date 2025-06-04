use octofit_db;

db.users.insertMany([
  { email: 'alice@example.com', name: 'Alice', password: 'alicepass' },
  { email: 'bob@example.com', name: 'Bob', password: 'bobpass' },
  { email: 'carol@example.com', name: 'Carol', password: 'carolpass' }
]);

db.teams.insertMany([
  { name: 'Team Alpha', members: ['alice@example.com', 'bob@example.com'] },
  { name: 'Team Beta', members: ['carol@example.com'] }
]);

db.activity.insertMany([
  { user: 'alice@example.com', activity_type: 'run', duration: 30, date: new Date() },
  { user: 'bob@example.com', activity_type: 'walk', duration: 45, date: new Date() },
  { user: 'carol@example.com', activity_type: 'strength', duration: 60, date: new Date() }
]);

db.leaderboard.insertMany([
  { team: 'Team Alpha', points: 150 },
  { team: 'Team Beta', points: 100 }
]);

db.workouts.insertMany([
  { user: 'alice@example.com', workout_type: 'cardio', details: '30 min run', date: new Date() },
  { user: 'bob@example.com', workout_type: 'walk', details: '45 min walk', date: new Date() },
  { user: 'carol@example.com', workout_type: 'strength', details: '60 min strength', date: new Date() }
]);
