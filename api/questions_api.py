import json

import requests

from api.client import Client


class Api(Client):
    USERS = '/users'
    BASE_URL = "https://reqres.in/api"

    def list_users(self):
        # method: get
        # rout: /users?page=2
        # status: 200

        url = self.BASE_URL + self.USERS + "?page=2"
        return self.get(url)

    def single_user_not_found(self):
        # method: get
        # rout: /users/23
        # status: 404

        url = self.BASE_URL + self.USERS + "/23"
        return self.get(url)

    def single_user(self):
        # method: get
        # rout: /users/2
        # status: 200

        url = self.BASE_URL + self.USERS + "/2"
        return self.get(url)

    def create(self, name, job):
        # method: get
        # rout: api/users
        # status: 201
        # body: {"name": "", "job": ""}

        url = self.BASE_URL + self.USERS
        payload = json.dumps({"name": F"{name}", "job": F"{job}"})
        headers = {"Content-Type": "application/json"}
        return self.post(url, headers, payload)

    def delete_user(self, id):
        # method: get
        # rout: api/users/id
        # status: 204
        url = self.BASE_URL + self.USERS + F"/{id}"
        return self.delete(url)

    def registration(self, email, password):
        """
                :method:    post
                :routs:     /api/register
                :status:    200
                :body:      {
                                "email": 'eve.holt@reqres.in'
                                "password": ''
                            }
                """

        url = self.BASE_URL + "/register"
        payload = json.dumps({
            "email": F"{email}",
            "password": F"{password}"
        })
        headers = {
            "Content-Type": "application/json"
        }
        return self.post(url, headers, payload)


api = Api()
