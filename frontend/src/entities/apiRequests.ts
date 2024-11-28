export const ApiRequestType = {
    GET: 'get',
    POST: 'post',
    PUT: 'put',
    DELETE: 'delete',
    PATCH: 'patch',
    HEAD: 'head',
    CONNECT: 'connect',
    TRACE: 'trace',
    OPTIONS: 'options',
}

export interface ApiRequest {
    url: string,
    type: string,
    headers: any,
    content: any,
}

export interface ApiResponse {
    url: string,
    code: number,
    headers: any,
    content: any,
}
