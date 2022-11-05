import http from "k6/http";
import { parseHTML } from 'k6/html';
export const options = {
 duration: "5s",
 vus: 10,
 summaryTrendStats: ["avg", "med", "p(95)", "p(99)"],
};
export function setup() {
  let port = __ENV.PORT
  let url = "http://localhost:"+port;
  let data = { url: 'https://google.com' };
  let res = http.post(url, data);
  const doc = parseHTML(res.body);
  url = doc.find('a').text();
  return { data: url };
}
export default function(data) {
 let port = __ENV.PORT
 http.get(data.data);
}
