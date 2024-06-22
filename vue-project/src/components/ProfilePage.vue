<template>
  <div class="profile-container">
    <h2>Profile Page</h2>
    <div class="profile-picture">
      <img v-if="profilePicture" :src="profilePicture" alt="Profile Picture" />
      <div v-else class="upload-icon" @click="uploadProfilePicture">
        <span>+</span>
      </div>
      <div v-if="profilePicture" class="picture-actions">
        <i class="fas fa-pencil-alt" @click="uploadProfilePicture"></i>
        
        <i class="fas fa-times" @click="deleteProfilePicture"></i>
      </div>
    </div>
    <div class="profile-field">
      <label>Display Name: </label>
      <span>{{ displayName }}</span>
    </div>
    <div class="profile-field">
      <label>Date of Birth: </label>
      <span>{{ dob }}</span>
    </div>
    <div class="profile-field">
      <label>Email Address: </label>
      <input v-model="email" type="email" placeholder="enter new email" />
    </div>
    <div class="profile-field">
      <label>Phone Number: </label>
      <input v-model="phoneNumber" type="text" placeholder="enter new phone number" />
    </div>
    <div class="profile-field">
      <label>Zipcode: </label>
      <input v-model="zipcode" type="text" placeholder="enter new zip" />
    </div>
    <div class="profile-field">
      <label>Password: </label>
      <input v-model="password" type="password" placeholder="enter new password here" />
    </div>
    <div class="profile-field">
      <label>Password Confirmation: </label>
      <input
        v-model="passwordConfirmation"
        type="password"
        placeholder="re- enter new password here"
      />
    </div>
    <button @click="updateProfile">Update</button>
    <br />
    <router-link to="/">Return to main page</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      displayName: 'Mihir Prakash',
      email: 'mp107@rice.edu',
      phoneNumber: '346-638-1871',
      zipcode: '77030',
      password: 'oldpass',
      passwordConfirmation: '',
      profilePicture: null,
      dob: '08/22/1996'
    }
  },
  methods: {
    updateProfile() {
      alert('Profile updated!')
    },
    uploadProfilePicture() {
      const fileInput = document.createElement('input')
      fileInput.type = 'file'
      fileInput.accept = 'image/*'
      fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0]
        const reader = new FileReader()
        reader.onload = (e) => {
          this.profilePicture = e.target.result
        }
        reader.readAsDataURL(file)
      })
      fileInput.click()
    },
    deleteProfilePicture() {
      this.profilePicture = null
    }
  }
}
</script>

<style scoped>
.profile-container {
  max-width: 500px;
  margin: 40px auto;
  padding: 1.5em;
  background: #f9f9f9;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border: 2px slategray black;
  
}
.profile-field {
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
.profile-picture {
  display: flex;
  justify-content: center;
  margin-bottom: 1em;
}

.profile-picture img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
}

.upload-icon {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: #f1f1f1;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 48px;
  color: #888;
}
i{
    margin-left: 10px;
}
</style>
