import React from "react";

import "./news.css";

interface NewsProps {
    name: string; 
    shortText: string;
    link: string;
}

export function News(props: NewsProps) {
    return (
        <>
            <div className="news-container">
                <b>{ props.name }</b>
                { props.shortText }
                <a href={ props.link } className="link">Читать далее...</a>
            </div>
            <span className="vertical-line" />
        </>
    );
}
