<template>
<div class="flex flex-row justify-between items-center py-4 px-8 bg-white dark:bg-gray-700">
  <h2 class="text-xl text-white">{{ title }}</h2>
  <div>
    <slot></slot>
  </div>
</div>
</template>

<script setup>
  defineProps({
    title: String
  });
</script>
