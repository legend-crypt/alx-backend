import { createClient } from 'redis';

function publishMessage(message, time) {
  const client = createClient();
  client.on('error', (error) =>
    console.log(`Redis client not connected to the server: ${error}`)
  );
  client.on('connect', () =>
    console.log('Redis client connected to the server')
  );
  setTimeout(() => {
    console.log(`About to send message ${message}`);
    client.publish('ALXchannel', message);
  }, time);
}

publishMessage('ALX Student #1 starts course', 100);
publishMessage('ALX Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('ALX Student #3 starts course', 400);
