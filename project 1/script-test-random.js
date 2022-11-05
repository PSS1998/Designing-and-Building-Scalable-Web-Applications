import http from "k6/http";
export const options = {
 duration: "5s",
 vus: 10,
 summaryTrendStats: ["avg", "med", "p(95)", "p(99)"],
};
export default function() {
 let port = __ENV.PORT
 http.get("http://localhost:"+port+"/random");
}
