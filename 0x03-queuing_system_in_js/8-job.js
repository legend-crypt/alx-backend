function createPushNotificationJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  for (const elem of jobs) {
    const job = queue.create('push_notification_code_3', elem);
    job
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id}`);
      })
      .on('progress', (progress, _) => {
        `Notification job ${job.id} ${progress}% complete`;
      })
      .on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
      });
    job.save();
  }
}
export default createPushNotificationJobs;
