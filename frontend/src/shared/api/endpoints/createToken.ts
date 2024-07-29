const axios = require('axios');

import { apiUrl } from "./apiUrl";

export async function createToken(
    nickname: string,
    password: string,
) {
    axios.post(apiUrl + "/auth/login")
        .then((response: any) => {
            console.log(response);
        })
}
