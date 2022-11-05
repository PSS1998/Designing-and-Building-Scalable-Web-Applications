FROM node:fermium-slim

EXPOSE 3000

WORKDIR /app

COPY . .

RUN npm install express
RUN npm install sqlite3
RUN npm install ejs
RUN npm install body-parser

CMD ["node", "index.js"]
