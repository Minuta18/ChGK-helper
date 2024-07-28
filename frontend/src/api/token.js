import * as api from './api.js';
import { useState, useCallback, useEffect } from 'react';
import { useCookies } from 'react-cookie';

export async function checkToken(token) {
    console.log('Token: ' + token);
    if (token === null || token === undefined) { return false; }
    const response = await fetch(api.urls.constructApiUrl('/auth/check'), {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }
    })
    return (response.status === 200);
}

export function useToken() {
    const [loading, setLoading] = useState(true);
    const [invalidToken, setInvalidToken] = useState(true);
    const [cookie, setCookie, removeCookie] = useCookies(['auth-token']);

    const checkToken = useCallback(async (cookie) => {
        let result = await api.tokens.checkToken(cookie);
        console.log(result);
        // if (!result) removeCookie('auth-token');
        return result;
    }, []);

    useEffect(() => {
        checkToken(cookie['auth-token']).then((res) => { 
            setInvalidToken(!res); 
        });
        setLoading(false);
    }, []);

    return [loading, invalidToken, cookie['auth-token']];
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
        const response = await fetch(api.urls.constructApiUrl('/auth/login'), {
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
