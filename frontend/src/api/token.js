import * as api from './base_url.js';

export async function checkToken(token) {
    console.log('Token: ' + token);
    if (token === null || token === undefined) { return false; }
    const response = await fetch(api.constructApiUrl('/auth/check'), {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }
    })
    return (response.status === 200);
}

export class AuthToken {
    constructor(token) {
        if (AuthToken._instance) {
            return AuthToken._instance;
        }
        AuthToken._instance = this;

        this.token = token;
    }

    getToken() { return this.token; }
    getAuthString() { return 'Bearer ' + this.token; }
    setToken(token) { this.token = token; }

    async fetchToken(
        username, password, onInvalidPassword, onInvalidUser, onError,
        onOkay,
    ) {
        const response = await fetch(api.constructApiUrl('/auth/login'), {
            method: 'POST',
            body: JSON.stringify({
                user_nickname: username,
                user_password: password,
            }),
            headers: {
                'Content-Type': 'application/json',
            }
        })

        if (response.status === 200) {
            const body = await response.json();
            this.token = body.token;
            // console.log(body.token);
            try { onOkay(); } catch (err) { console.log(err); }
        } else if (response.status === 401) {
            onInvalidPassword();
        } else if (response.status === 404) {
            onInvalidUser();
        } else if (response.status === 500) {
            onError();
        }
    }
}
