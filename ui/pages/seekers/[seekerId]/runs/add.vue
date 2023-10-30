<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <section-header title="Create run" />
    <div class="mx-auto p-8">
      <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
        <div class="relative p-4 w-full max-w-2xl h-full md:h-auto">
            <FormKit action="#" type="form" @submit="initiateRun" :disabled="loading">
              <FormKit
                type="text"
                name="name"
                id="name"
                label="Name"
              />
              <FormKit
                type="number"
                name="from_timestamp"
                id="from_timestamp"
                min="0"
                step="1"
                label="From timestamp"
              />
              <FormKit
                type="number"
                name="to_timestamp"
                id="to_timestamp"
                min="0"
                step="1"
                label="To timestamp"
              />
            </FormKit>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
  import { initModals } from 'flowbite'
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()
  const loading = useState(() => false)

  onMounted(() => {
    initModals()
  })

  const initiateRun = async (runData) => {
    loading.value = true

    const result = await $fetch(
      `${config.public.apiRoot}/runs/`, {
        method: 'POST',
        body: { ...runData, seeker: route.params.seekerId }
      }
    )

    loading.value = false

    router.replace({ path: `/seekers/${route.params.seekerId}/runs` })

    console.log(result)
  }
</script>
