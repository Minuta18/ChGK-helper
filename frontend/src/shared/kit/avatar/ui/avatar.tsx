import React from "react";

import {ReactComponent as DefaultAvatar} from "../assets/default-avatar.svg";

interface AvatarProps {
    link?: string;
}

export function Avatar({ link }: AvatarProps) {
    return (
        <>
            {
                (link === null || link === undefined) ?
                <DefaultAvatar /> :
                <img className="avatar" src="fuck" alt="" />
            }
        </>
    );
}