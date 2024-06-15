<template>
  <div>
  <NavbarComponent />
    <h1>My Feed</h1>
    <table class="tbl">
      <tr v-for="(row, rowIndex) in rows" :key="rowIndex">    //each item in array rows represents a row
        <td v-for="(post, postIndex) in row" :key="postIndex"> //we have a post item in each subarray row [{p1},{p2}]
          <div v-if="post.type === 'text'" class="textDiv">
            {{ post.content }}
          </div>
          <div v-else>
            <img :src="post.images[post.currentImageIndex]" :alt="'Image ' + post.currentImageIndex" />
            <button @click="toggleInterval(rowIndex, postIndex)">{{ post.intervalId ? 'Stop' : 'Start' }}</button>
            <p>{{ post.content }}</p>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import NavbarComponent from './Navbar.vue';
export default {
  components: {
  NavbarComponent,
},
  data() {
    return {
      posts: [
        { type: 'text', 
        content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nulla velit, accumsan eget neque eu, eleifend imperdiet metus. Phasellus ut vehicula leo. Aenean cursus eros vel luctus pharetra. Sed ut enim in arcu vestibulum eleifend in non nisl. Sed eget tempus metus, sed lobortis metus. Mauris viverra, ex ac aliquam porta, libero orci volutpat sapien, et malesuada metus nulla condimentum est. Sed dapibus tempus felis, vitae pulvinar elit hendrerit vel. Donec est velit, pulvinar eu nibh ac, posuere bibendum tortor. Nunc fringilla, est sit amet pellentesque lacinia, nunc nibh aliquet diam, eu faucibus nisl enim dapibus risus.' },
        {
          type: 'image',
          content: 'Townhouses -->Lorem ipsum dolor sit amet...',
          images: ['https://images.unsplash.com/photo-1672610444491-2284fefdd735?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cm93aG91c2VzfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1689214718217-1beaebb918bf?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHJvd2hvdXNlc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1470260453955-6e918f763fc9?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHJvd2hvdXNlc3xlbnwwfHwwfHx8MA%3D%3D'],
          currentImageIndex: 0,
          intervalId: null,
        },
        {
          type: 'image',
          content: 'Penthouse-->Lorem ipsum dolor sit amet...',
          images: ['https://images.unsplash.com/photo-1565623833408-d77e39b88af6?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGVudGhvdXNlfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1542928658-22251e208ac1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGVudGhvdXNlfGVufDB8fDB8fHww', 
          'https://images.unsplash.com/photo-1609766857326-18a204c2cf31?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGVudGhvdXNlfGVufDB8fDB8fHww'],
          currentImageIndex: 0,
          intervalId: null,
        },
        { type: 'text', content: 'Another text post...Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nulla velit, accumsan eget neque eu, eleifend imperdiet metus. Phasellus ut vehicula leo. Aenean cursus eros vel luctus pharetra. Sed ut enim in arcu vestibulum eleifend in non nisl. Sed eget tempus metus, sed lobortis metus. Mauris viverra, ex ac aliquam porta, libero orci volutpat sapien, et malesuada metus nulla condimentum est. Sed dapibus tempus felis, vitae pulvinar elit hendrerit vel. Donec est velit, pulvinar eu nibh ac, posuere bibendum tortor. Nunc fringilla, est sit amet pellentesque lacinia, nunc nibh aliquet diam, eu faucibus nisl enim dapibus risus' },
        {
          type: 'image',
          content: 'Mansions--> Lorem ipsum dolor sit amet...',
          images: ['https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8TWFuc2lvbnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1593714604578-d9e41b00c6c6?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8TWFuc2lvbnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1505843513577-22bb7d21e455?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8TWFuc2lvbnN8ZW58MHx8MHx8fDA%3D'],
          currentImageIndex: 0,
          intervalId: null,
        },
        
        {
          type: 'image',
          content: 'Beach Villa --> Lorem ipsum dolor sit amet...',
          images: ['https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhY2glMjB2aWxsYXxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1578439297699-eb414262c2de?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGJlYWNoJTIwdmlsbGF8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1605538032432-a9f0c8d9baac?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGJlYWNoJTIwdmlsbGF8ZW58MHx8MHx8fDA%3D'],
          currentImageIndex: 0,
          intervalId: null,
        }
        
        
        
      ],
    };
  },
  computed: {
    rows() {
      const rows = [];
      for (let i = 0; i < this.posts.length; i += 2) {
        rows.push(this.posts.slice(i, i + 2));
      }
      return rows;
    },
  },
  methods: {
    toggleInterval(rowIndex, postIndex) {
      const post = this.rows[rowIndex][postIndex]; //retrieves the specific post
      if (post.intervalId) { //it means an interval (timer) is currently running for this post’s image rotation.
        clearInterval(post.intervalId); //Clears (stops) the interval associated with this post.
        post.intervalId = null; //Resets intervalId to null, indicating no timer is active for this post.
      } else {
        const intervalTime = Math.floor(Math.random() * 5 + 1) * 1000; //We generate a random interval time 
        post.intervalId = setInterval(() => {
          post.currentImageIndex = (post.currentImageIndex + 1) % post.images.length;
        }, intervalTime); //Modulo used for handling the rotation of images in a cyclic manner. Using % post.images.length ensures that post.currentImageIndex stays within the bounds of the post.images array. 
      }
    },  
  },
  beforeDestroy() { //is a lifecycle hook
    for (const post of this.posts) {
      if (post.intervalId) {
        clearInterval(post.intervalId);
      }
    }
  },
};
</script>
  
<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

td {
  border: 1px solid #ccc;
  padding: 16px;
  width: 50%;
  vertical-align: top;
}



button {
  margin-top: 8px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #0056b3;
}
img{
  height: 300px;
  width: 400px;
  border-radius: 12px;
  margin: 15px;
}

tr,td{
  box-shadow: 10px 10px 5px rgba(0,0,0,0.05);   
  
  
}
.textDiv{
  
  margin-top: 80px;
  font-weight: 500;
}
</style>