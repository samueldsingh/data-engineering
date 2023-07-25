
# What is supabase?
  Supabase is a real-time database platform that includes built-in support for authentication. This means that you can easily implement 
authentication for your web or mobile app using Supabase without setting up and managing your authentication server.

- A complete backend for web and mobile applications based entirely on free open source software.
- Biggest challenge when building app - is not writing code - it's architecting a system to work at scale.
- Firebase and amplify have addressed the barrier but one big problem is they lock you into propritery technology that works on a specific cloud platform.
- Supabase is a firebase alternative and at high level it provides two things; at backend we have infrastructure like database file storage and edge functions that
  run on the cloud; on frontend we have client-side SDK's that can easily connect this infrastructure to a frontend framework

Advantages:
- You can manage postgres database with an easy to understand UI which automatically generates REST and GraphQL to use in your code
- Database integrates directly with user authentication making it trivial to implement row level security.
- Like firebase, it can listen to changes in real time while scaling to virtually any workload.

Getting started:
- You can use Docker to self-host or sign up with supabase for a fully managed account that starts with a free tier.
- On dashboard, you can create tables in your postgres database with a click of a button.
- You can insert columns to build out your schema and then add new rows to populate it with data.
- By default every project has an authentication schema to manage users within the application..
- This opens door to row level security where you write policies to who has access to your data.
- Database supports triggers to react to changes in your data and postgres functions to run stored procedures directly on the database server.
- Generates custom API documentation from where you can copy queries tailored to your database and use them in a javascript project.
- Install supabase SDK with npm, connect to your project, sign in with a single line of code and now we can listen to any changes in authentication state in
  real time with on off stage.
- When it comes to database, we don't need to write raw sql, instead we can post javascript code from the API or use the REST and GraphQL APIs directly.
  
