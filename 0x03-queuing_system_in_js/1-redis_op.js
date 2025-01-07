import { createClient, print } from 'redis';

let redisClient;
redisClient = createClient();
redisClient.on('error', (error) => console.error(`Error: ${error}`));
redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  redisClient.SET(schoolName, value, print);
  console.log(print);
}

function displaySchoolValue(schoolName) {
  redisClient.GET(schoolName, (_err, result) => {
    console.log(result);
  });
}
displaySchoolValue('ALX');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
