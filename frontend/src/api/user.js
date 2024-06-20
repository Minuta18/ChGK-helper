import * as api from './base_url.js';

export async function createUser(nickname, email, password, responseHandler) {
    try {
        const response = await fetch(api.constructApiUrl('/users/'), {
            method: 'POST',
            body: JSON.stringify({
                email: email,
                nickname: nickname,
                password: password,
            }),
            headers: {
                'Content-Type': 'application/json'
            },
        });
        const body = await response.json();
        const status = response.status;
        // console.log(status, body);
        return [status, body];
    } catch (err) {
        console.error(err);
    }
}
