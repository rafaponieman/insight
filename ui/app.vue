<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
  useHead({
    htmlAttrs: {
      class: 'dark'
    },
    bodyAttrs: {
      class: 'antialiased dark:bg-gray-900'
    }
  })
</script>
