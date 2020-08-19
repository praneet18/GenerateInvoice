function addrow() {
    var tbody = document.getElementById('tab_logic_body');
    var row = tbody.insertRow()
    var input = document.createElement('input')
    input.setAttribute("type", "text")
    var child = tbody.children.length
    for (var i = 0; i < 5; i++) {
        var cell = row.insertCell();
        if (i == 0) {
            cell.innerHTML = child;
        }
        else {
            var input = document.createElement('input');
            cell.appendChild(input);
            switch (i) {
                case 1:
                    var name = 'product'
                    var type = "text";
                    var placeholder = "Enter Product Name";
                    break;
                case 2:
                    var name = 'quantity'
                    var type = "number";
                    var placeholder = "Enter Qty";
                    break;
                case 3:
                    var name = 'price'
                    var type = "number";
                    var placeholder = "Enter Unit Price";
                    break;
                case 4:
                    var name = 'total'
                    var type = "number";
                    var placeholder = "0.00";
                    break;
            }
            input.setAttribute("type", type)
            input.setAttribute("id", name + child)
            input.setAttribute("name", name)
            input.setAttribute("placeholder", placeholder)
            input.setAttribute("class", "form-control " + name)
            if (i == 4) {
                input.readOnly = true;
            }
        }

    }
    $(document).ready(function (e) {
        $("input[name='quantity']").change(function () {
            var optionSelected = $("option:selected", this);
            calc(this);
        });
    });
    $(document).ready(function (e) {
        $("input[name='price']").change(function () {
            var optionSelected = $("option:selected", this);
            calc(this);
        });
    });
}

function deleterow() {
    var tbody = document.getElementById('tab_logic_body');
    if (tbody.children.length == 1)
        alert('Atleast 1 row is Required')
    else {
        tbody.deleteRow(tbody.rows.length - 1);
    }
};

$(document).ready(function (e) {
    $("input[name='quantity']").change(function () {
        var optionSelected = $("option:selected", this);
        calc(this);
    });
});
$(document).ready(function (e) {
    $("input[name='price']").change(function () {
        var optionSelected = $("option:selected", this);
        calc(this);
    });
});

function calc(input) {
    if (input.id.includes("price")) {
        var id = input.id.replace('price', 'quantity')
        var idt = input.id.replace('price', 'total')
    }
    else {
        var id = input.id.replace('quantity', 'price')
        var idt = input.id.replace('quantity', 'total')
    }
    let s = document.getElementById(id)
    if (s.value != '') {
        total = s.value * input.value
        document.getElementById(idt).value = total
        calctotal();
    }
};

function calctotal() {
    var total = document.getElementsByName('total')
    subtotal = 0
    for (var i = 0; i < total.length; i++) {
        subtotal += parseFloat(total[i].value)
    }
    document.getElementById('sub_total').value = subtotal
    var tax = document.getElementById('tax')
    var taxAmount = (tax.value * subtotal) / 100

    document.getElementById('tax_amount').value = taxAmount
    document.getElementById('total_amount').value = subtotal + taxAmount
}

$(document).ready(function (e) {
    $("#tax").change(function () {
        var optionSelected = $("option:selected", this);
        calctotal();
    });
});

(function () {
    console.log(document.getElementById('total_amount'))
});