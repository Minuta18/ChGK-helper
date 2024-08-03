import * as ReactRedux from "react-redux";

export function useUserData() {
    const { userToken, userData } = ReactRedux.useSelector(
        (state: any) => state.auth
    );

    if (userToken === null) {
        return null;
    } else {
        return {
            token: userToken,
            data: userData,
        };
    }
}
