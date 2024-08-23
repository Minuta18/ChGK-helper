import React from 'react';

import './labels.css';

export function ErrorLabel(props) {
    return (<>
        { props.hidden ?
            <label className='hidden-label'>
                { props.children }
            </label> :
            <label className='error-label'>
                { props.children }
            </label>
        }
    </>);
}
