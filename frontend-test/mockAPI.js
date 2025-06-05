const jobs = {};

export function startJob() {
  const jobId = `job-${Math.random().toString(36).slice(2)}`;
  jobs[jobId] = {
    status: 'pending',
    createdAt: Date.now(),
  };

  // Simulate status transitions over time
  setTimeout(() => jobs[jobId].status = 'processing', 2000);
  setTimeout(() => {
    const fail = Math.random() < 0.1; // 10% fail chance
    jobs[jobId].status = fail ? 'failed' : 'done';
  }, 8000);

  return Promise.resolve({ jobId });
}

export function getJobStatus(jobId) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        jobId,
        status: jobs[jobId]?.status || 'unknown',
      });
    }, 300); // simulate network delay
  });
}

