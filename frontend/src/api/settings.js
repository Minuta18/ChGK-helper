import * as api from './api.js';

export async function fetchSettingsRequest(
        userId, token, onUnauthorizedCallback
    ) {
    try {
        const response = await fetch(
            api.urls.constructApiUrl('/users/settings/' + userId), {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            }
        );
        if (response.status === 401) {
            onUnauthorizedCallback();
        } else if (response.status === 200) {
            const body = await response.json();
            console.log(body);
            return [
                body.user.time_for_reading, 
                body.user.time_for_solving, 
                body.user.time_for_typing,
            ];
        } else {
            console.error(response);
        }
    } catch (err) {
        console.error(err);
    }
}

export async function updateSettings(
        userId, token, onUnauthorizedCallback, onErrorCallback, 
        timeForReading, timeForSolving, timeForTyping,
    ) {
    try {
        const response = await fetch(
            api.urls.constructApiUrl('/users/settings/' + userId), {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body: JSON.stringify({
                    'time_for_reading': timeForReading,
                    'time_for_solving': timeForSolving,
                    'time_for_typing': timeForTyping,
                }),
            }
        );
        if (response.status === 401) {
            onUnauthorizedCallback();
        } else {
            onErrorCallback();
        }
    } catch (err) {
        console.error(err);
    }
}

export class Settings {
    constructor() {
        if (Settings._instance) {
            return Settings._instance;
        }
        Settings._instance = this;

        this.time_for_reading = 0;
        this.time_for_solving = 0;
        this.time_for_typing = 0;
    }

    async fetchSettings(userId, token, onUnauthorizedCallback) {
        let result = await fetchSettingsRequest(userId, token, () => {
            onUnauthorizedCallback();
        });
        console.log(result);
        return result;
    }

    setSettings(time_for_reading, time_for_solving, time_for_typing) {
        this.time_for_reading = time_for_reading;
        this.time_for_solving = time_for_solving;
        this.time_for_typing = time_for_typing;
    }

    getSettings() {
        return [
            this.time_for_reading, 
            this.time_for_solving, 
            this.time_for_typing,
        ];
    }
}
