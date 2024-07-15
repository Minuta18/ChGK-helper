// DEPRECATED! Please use constructApiUrl() instead
export const baseUrl = 'http://localhost:5000/api/v1';

export function constructApiUrl(url) {
    return baseUrl + url;
}
