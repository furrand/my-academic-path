FROM node:18-alpine

WORKDIR /app/frontend

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]

# The commands below are for serving the production build

# TODO: I'll figure out a better way to create separate dockerfiles for local/prod
# environments when we get closer to deploying.

# FROM node:18-alpine
#
# WORKDIR /app
#
# COPY package.json .
#
# RUN npm install
#
# RUN npm i -g serve
#
# COPY . .
#
# RUN npm run build
#
# EXPOSE 3000
#
# CMD [ "serve", "-s", "dist" ]

