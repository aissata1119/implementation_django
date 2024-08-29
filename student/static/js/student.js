function openModal() {
   id=event.target.getAttribute('data-id')
   document.getElementById('deleteModal').classList.remove('hidden');
}


function closeModal() {
   document.getElementById('deleteModal').classList.add('hidden');
}

function deleteItem() {
   window.location.href=id
   closeModal();
}
