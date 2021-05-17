import React from 'react';

import './styles.css'

export default class Login extends React.Component {
    render() {
        return (
            <div className="Login">
                <div className="main_container">

                    <div className="form_wrapper">
                        <form name="login_form" id="login_form" action="" method="post">

                            <h2>Login</h2>

                            <fieldset>
                                <legend>usuário</legend>
                                <input type="text" name="username" id="username" />
                            </fieldset>

                            <fieldset>
                                <legend>senha</legend>
                                <input type="password" name="password" id="password" />
                            </fieldset>

                            <input type="checkbox" name="remember_me_checkbox" id="remember_me_checkbox" />
                            <label htmlFor="remember_me_checkbox">lembrar-me</label>

                        </form>
                    </div>

                    <button type="submit" onClick={submitForm}>Entrar</button>

                </div>
            </div>
        );
    }
}

function submitForm(): React.MouseEventHandler<HTMLButtonElement> | undefined {
    const form: HTMLFormElement = document.getElementById('login_form') as HTMLFormElement;
    form.submit()
    return undefined
}

