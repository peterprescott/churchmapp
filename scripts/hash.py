# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,rmd//Rmd,scripts//py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Demonstrate Password Hashing

from passlib.hash import pbkdf2_sha256


# this is the `authenticate()` function for the backend server
def authenticate():
    try:
        email = request.json['email']
        password = request.json['password']

        user = session.query(User)\
                    .filter(User.email==email)\
                    .first()
        if user: # if user already exists...
            # ... authenticate password
            if not pbkdf2_sha256\
                    .verify(
                        password,
                        user.password_hash
                        ):
                return jsonify(
                    {'message':'Wrong password for that email'}
                    ), 401
            else:
                message = 'Authentication successful'

        else: # else create new password hash and user
            hash = pbkdf2_sha256.hash(password)
            user = User(email=email, password_hash=hash)
            session.add(user)
            session.commit()
            message = 'Registration successful'

        # everyone still here gets a token
        payload = { 'email': email }
        token = jwt.generate_jwt(
            payload, JWT_security_key, 
            'PS256', timedelta(minutes=15))
        return jsonify({
            'message': message, 
            'JWT': token
                    }), 202

    except Exception as e:
        return jsonify({'error':str(e)[:100]}), 500


# let's just look at what pbkdf2_sha256 does
password = 'secret'
print(password)
hash = pbkdf2_sha256.hash(password)
print(hash)
authenticate = pbkdf2_sha256.verify('wrong password', hash)
print(authenticate)
authenticate = pbkdf2_sha256.verify(password, hash)
print(authenticate)
