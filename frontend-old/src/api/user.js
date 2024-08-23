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
                'Content-Type': 'application/json',
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

export async function getUserId(token, onUnauthorizedCallback) {
    try {
        const response = await fetch(
            api.constructApiUrl('/users/self'), {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
        })
        if (response.status !== 200) {
            // onUnauthorizedCallback();
            // alert('Unauthorized: ' + token);
            return null;
        } else {
            const body = await response.json();
            console.log('Result: ' + body.id);
            return body.id;
        }
    } catch (err) {
        console.error(err);
        alert('Error: ' + err);
    }
}
