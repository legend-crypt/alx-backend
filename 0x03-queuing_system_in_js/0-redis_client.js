import { createClient } from 'redis';

let redisClient;
redisClient = createClient();
redisClient.on('error', (error) => console.error(`Error: ${error}`));
redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});
