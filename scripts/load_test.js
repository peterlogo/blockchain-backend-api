import http from "k6/http";
import { sleep } from "k6";

export let options = {
  stages: [
    { duration: "10s", target: 100 }, // Ramp up to 100 RPS in 10 seconds
    { duration: "30s", target: 100 }, // Maintain 100 RPS for 30 seconds
    { duration: "10s", target: 0 }, // Ramp down to 0 RPS
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests should be below 500ms
    http_req_failed: ["rate<0.01"], // Fail rate should be < 1%
  },
};

export default function () {
  let res = http.get("http://localhost:8000/transactions"); // Update with your actual API URL
  console.log(
    `Response time: ${res.timings.duration}ms, Status: ${res.status}`
  );

  sleep(1); // Helps distribute requests evenly
}
