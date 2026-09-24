window.onload = function() {
    fetchPatients();
};

async function fetchPatients() {
    try {
        const response = await fetch('/api/patients');
        const patients = await response.json();
        const tbody = document.getElementById('patientTableBody');
        tbody.innerHTML = "";

        patients.forEach(patient => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${patient[0]}</td>
                <td>${patient[1]}</td>
                <td>${patient[2]}</td>
                <td>${patient[3]}</td>
                <td><span class="badge-registered">Registered</span></td>
            `;
            tbody.appendChild(tr);
        });

        document.getElementById('totalPatientsCount').innerText = patients.length;
    } catch (error) {
        console.error("Error fetching patients:", error);
    }
}

async function registerPatient() {
    const id = document.getElementById('regId').value.trim();
    const name = document.getElementById('regName').value.trim();
    const age = document.getElementById('regAge').value.trim();
    const gender = document.getElementById('regGender').value;

    if (!id || !name || age === "") {
        alert("Please fill in all patient details.");
        return;
    }

    const response = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id, name, age: parseInt(age), gender })
    });

    const data = await response.json();
    const successBanner = document.getElementById('successBanner');

    if (data.status === "success") {
        successBanner.innerText = `Patient ${name} (${id}) registered successfully!`;
        successBanner.style.display = 'block';
        fetchPatients();
        setTimeout(() => {
            successBanner.style.display = 'none';
            switchTab('history', document.querySelectorAll('nav a')[3]);
        }, 1500);
    } else {
        alert("Error registering patient.");
    }
}