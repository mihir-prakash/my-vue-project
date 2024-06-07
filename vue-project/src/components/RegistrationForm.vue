<template>
    <div>
      <form @submit.prevent="validateForm">
        <h1>Register</h1>
        <div>
          <label>Account Name:</label>
          <input v-model="form.accountName" required placeholder="account name"/>
        </div>
        <div>
          <label>Display Name:</label>
          <input v-model="form.displayName" placeholder="display name (optional)"/>
        </div>
        <div>
          <label>Email Address:</label>
          <input v-model="form.email" type="email" required placeholder="email"/>
        </div>
        <div>
          <label>Phone Number:</label>
          <input v-model="form.phoneNumber" type="tel" required  placeholder="phone"/>
        </div>
        <div>
          <label>Date of Birth:</label>
          <input v-model="form.dob" type="date" required />
        </div>
        <div>
          <label>Zipcode:</label>
          <input v-model="form.zipcode" required placeholder="zipcode"/>
        </div>
        <div>
          <label>Password:</label>
          <input v-model="form.password" type="password" required placeholder="password" />
        </div>
        <div>
          <label>Confirm Password:</label>
          <input v-model="form.confirmPassword" type="password" required placeholder="re-enter password" />
        </div>
        <input type="hidden" v-model="form.timestamp" />
        <div>
          <button type="button" @click="clearForm">Clear</button>
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          accountName: '',
          displayName: '',
          email: '',
          phoneNumber: '',
          dob: '',
          zipcode: '',
          password: '',
          confirmPassword: '',
          timestamp: ''
        }
      };
    },
    methods: {
      clearForm() {
        this.form = {
          accountName: '',
          displayName: '',
          email: '',
          phoneNumber: '',
          dob: '',
          zipcode: '',
          password: '',
          confirmPassword: '',
          timestamp: ''
        };
      },
      validateForm() {
        this.form.timestamp = Date.now(); //our timestamp property updates just after the user clicks submit!!
  
        if (!this.validateEmail(this.form.email)) {
          alert('Invalid email address');
          return;
        }
  
        if (!this.validatePhoneNumber(this.form.phoneNumber)) {
          alert('Invalid phone number');
          return;
        }
  
        if (this.calculateAge(this.form.dob) < 18) {
          alert('You must be at least 18 years old to register');
          return;
        }
  
        if (this.form.password !== this.form.confirmPassword) {
          alert('Passwords do not match');
          return;
        }
  
        alert('Form submitted successfully');
        
      },
      validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
      },
      validatePhoneNumber(phoneNumber) {
        const re = /^\d{10}$/; 
        return re.test(phoneNumber);
      },
      calculateAge(dob) {
        const birthDate = new Date(dob);
        const difference = Date.now() - birthDate.getTime();
        const ageDate = new Date(difference);
        return Math.abs(ageDate.getUTCFullYear() - 1970);
      }
    }
  };
  </script>
  
  <style scoped>
form {
  max-width: 500px;
  margin: 0 auto;
  padding: 1.5em;
  background: #f9f9f9;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border: 2px slategray black;
}

form div {
  margin-bottom: 1em;
  display: flex;
  align-items: center;
}

label {
  display: inline-block;
  width: 120px;
  text-align: right;
  margin-right: 1em;
}

input {
  flex: 1;
  padding: 0.5em;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button {
  padding: 0.5em 1em;
  font-size: 1em;
  border: none;
  border-radius: 3px;
  background: #007bff;
  color: white;
  cursor: pointer;
  margin-right: 1em;
}

button:disabled {
  background: #ccc;
}

button:hover:not(:disabled) {
  background: #0056b3;
}
</style>

  