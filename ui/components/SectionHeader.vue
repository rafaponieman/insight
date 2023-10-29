<template>
<div class="flex flex-row justify-between items-center py-4 px-8 bg-white dark:bg-gray-700">
  <h2 class="text-xl text-white">{{ title }}</h2>
  <a href="add-product.html" class="btn relative flex flex-row items-center justify-center gap-x-2 py-2 px-4 rounded-[6.25rem] hover:shadow-md text-sm tracking-[.00714em] font-medium bg-primary-600 text-white dark:bg-primary-200 dark:text-primary-800">
    <span class="material-symbols-outlined">add</span>
      Add New
  </a>
</div>
</template>

<script setup>
  defineProps({
    title: String
  });
</script>
