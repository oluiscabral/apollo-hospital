import React from 'react';
import { Route, Redirect, RouteProps } from 'react-router-dom';

export default class ProtectedRoute extends Route {
    constructor(props: RouteProps) {
        super(props);
    }

    render() {
        let isAuthenticated = true;


        return isAuthenticated ? (
            this.props.children
        ) : (
            <Redirect to={{ pathname: '/login' }} />
        );
    }
}
