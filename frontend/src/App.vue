<template>
<Suspense> 
<div class="accordion" id="accordionExample">
  <div class="accordion-item" v-for="item in response">
    <h2 class="accordion-header" id="headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
      {{ item.name }}
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <ul class="list-group">
            <li class="list-group-item" aria-current="true" v-for="product in item.products">{{product.title}}</li>
          </ul>
      </div>
    </div>
  </div>
 
    </div>
</Suspense> 
</template>

<style lang="scss">


</style>

<script setup>
import axios from 'axios'
import { ref } from 'vue';
const response = ref([])



const fetchData = async () => {
  const {data}=await(axios.get('http://127.0.0.1:8000/categories_of_products'))
  response.value = data
  console.log(data)
}

fetchData()


</script>
