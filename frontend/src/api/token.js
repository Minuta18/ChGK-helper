import * as api from './base_url.js';
import Cookies from 'universal-cookie';

export function getFromCookies() {
    const cookies = new Cookies(null, {path: '/'});
    return cookies.get('auth-token');
}

export function removeFromCookies() {
    const cookies = new Cookies(null, {path: '/'});
    cookies.remove('auth-token');
}

export function saveToCookies(token) {
    const cookies = new Cookies(null, {path: '/'});
    let expire_date = new Date(Date.now());
    expire_date.setFullYear(expire_date.getFullYear() + 1);
    cookies.set('auth-token', token, {
        expires: expire_date,
    });
}

export function checkToken() {
    const token = getFromCookies();
    if (token === null || token === undefined) { return false; }
    let valid = false;
    fetch(api.constructApiUrl('/auth/check'), {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }
    }).then((response) => response.json())
      .then((json) => { valid = !json.error; });
    if (!valid) { removeFromCookies(''); }
    return valid;
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
            saveToCookies(this.token); 
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
