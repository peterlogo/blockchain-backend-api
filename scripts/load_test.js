import http from "k6/http";
import { check, sleep } from "k6";

// Test configuration
export let options = {
  scenarios: {
    steady_load: {
      executor: "constant-arrival-rate",
      rate: 100, // 100 requests per second
      timeUnit: "1s",
      duration: "3m", // Run for 3 minutes
      preAllocatedVUs: 50, // Pre-allocate virtual users
      maxVUs: 200, // Allow up to 200 virtual users
    },
  },
  thresholds: {
    http_req_duration: ["p(95)<1000"], // 95% of requests should be <1s
    http_req_failed: ["rate<0.02"], // Failure rate should be <2%
  },
};

export default function () {
  let res = http.get("http://localhost:8000/transactions");

  // Validate responses
  check(res, {
    "status is 200": (r) => r.status === 200,
    "response time < 1s": (r) => r.timings.duration < 1000,
  });

  sleep(0.1); // Small delay to simulate real user pacing
}
