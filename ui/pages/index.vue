<template>
  <div></div>
</template>

<script setup>
  const router = useRouter()

  onMounted(() => {
    router.replace({ path: '/seekers' })
  })
</script>
