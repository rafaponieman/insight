<template>
  <div class="mx-auto p-8">
    <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th v-for="column in props.columns" scope="col" class="px-4 py-3">{{ column.label }}</th>
              <th scope="col" class="px-4 py-3">
                  <span class="sr-only">Actions</span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in data" class="border-b dark:border-gray-700">
              <th scope="row" class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ item[columns[0].name] }}
              </th>
              <td v-for="(col, index) in columns.slice(1)" class="px-4 py-3">
                <listing-item
                  :additionalData="col.type === 'additional' ? additional[index - columns.length + additional.length + 1] : null"
                  :column="col"
                  :index="index"
                  :item="item"
                />
                </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps({
    columns: {
      type: Array,
      required: true
    },
    data: {
      type: Array,
      required: true
    },
    additional: {
      type: Array,
      required: false,
      default: []
    }
  })
</script>
