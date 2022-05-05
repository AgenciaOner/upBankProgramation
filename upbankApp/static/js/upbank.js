function mostrar(id, id02) {
   
    var display = document.getElementById(id).style.display;
    var display02  = document.getElementById('loasCidade').style.display;
    var h4s = document.querySelectorAll("h4")
    h4s.forEach((h4) => {
        h4.style.display = 'none';
    });
    
    if (id == 'loasBrasil') {
        if (display == 'block' && display02 == 'block') {
            document.getElementById(id).style.display = 'none';
            document.getElementById('loasCidade').style.display = 'none';


        }else {
            document.getElementById(id).style.display = 'block';
            document.getElementById('loasCidade').style.display = 'block';


        }    
    }
    if (display == 'block' && id != 'loasBrasil') {
        document.getElementById(id).style.display = 'none';
    } else {
        document.getElementById(id).style.display = 'block';
    }
    
    
    
    
    if (id02 == "#id_cliente-0-loas_0") {
        
        BMG = document.querySelector("#id_bmgCliente-0-INSS_0")
        BMG.checked = false
        SIAPE = document.querySelector("#id_siapeCliente-0-SIAPE_0")
        SIAPE.checked = false
        REFIN = document.querySelector("#id_refinCliente-0-REFIN_0")
        REFIN.checked = false
        OLE = document.querySelector("#id_oleCliente-0-OLE_0")
        OLE.checked = false
        BARI = document.querySelector("#id_bariCliente-0-BARI_0")
        BARI.checked = false
    
    
    } else if (id02 == "#id_bmgCliente-0-INSS_0") {
        
        SIAPE = document.querySelector("#id_siapeCliente-0-SIAPE_0")
        SIAPE.checked = false
        REFIN = document.querySelector("#id_refinCliente-0-REFIN_0")
        REFIN.checked = false
        OLE = document.querySelector("#id_oleCliente-0-OLE_0")
        OLE.checked = false
        BARI = document.querySelector("#id_bariCliente-0-BARI_0")
        BARI.checked = false
    }else if(id02 == "#id_siapeCliente-0-SIAPE_0"){
        REFIN = document.querySelector("#id_refinCliente-0-REFIN_0")
        REFIN.checked = false
        OLE = document.querySelector("#id_oleCliente-0-OLE_0")
        OLE.checked = false
        BARI = document.querySelector("#id_bariCliente-0-BARI_0")
        BARI.checked = false
    }else if(id02 == "#id_refinCliente-0-REFIN_0"){
        OLE = document.querySelector("#id_oleCliente-0-OLE_0")
        OLE.checked = false
        BARI = document.querySelector("#id_bariCliente-0-BARI_0")
        BARI.checked = false
    } else if(id02 == "#id_oleCliente-0-OLÉ_0"){
        BARI = document.querySelector("#id_bariCliente-0-BARI_0")
        BARI.checked = false    
    }
}
    
function enviar() {
    
    ids1 = document.querySelector("#ident01")
    ids2 = document.querySelector("#ident02")
    ids3 = document.querySelector("#ident03")
    ids4 = document.querySelector("#ident04")
    ids5 = document.querySelector("#ident05")
    ids6 = document.querySelector("#ident06")
    ids7 = document.querySelector("#ident07")
    ids8 = document.querySelector("#ident08")
    ids9 = document.querySelector("#ident09")
    ids10 = document.querySelector("#ident10")
    ids11 = document.querySelector("#id_selecione_0")
    ids12 = document.querySelector("#id_selecione_1")
    if (ids1.checked  == false || ids2.checked  == false || ids3.checked  == false || ids4.checked  == false || ids5.checked  == false || ids6.checked  == false ||  ids7.checked  == false ||  ids8.checked  == false ||
        ids9.checked  == false) {
        alert("Por favor preencha todos os campos! ")
    }else if(ids11.checked  == false && ids12.checked  == false){
        alert("Faltam campos para preencher! ")
    }else if (ids10.checked  == false){
        alert("Faltam campos para preencher! ")
    }else {
        alert("Parabéns, você acaba de adquirir programação UpBank, embreve nosso comercial entrará em contato!") 
           
    }

}
function verificacaoCampos() {
    
    loasBrasil = document.querySelector("#id_cliente-0-loas_0")
    loasCidade = document.querySelector("#id_cliente-0-loas_1")
    bmg = document.querySelector("#id_bmgCliente-0-INSS_0")
    siape  = document.querySelector("#id_siapeCliente-0-SIAPE_0")
    refin = document.querySelector("#id_refinCliente-0-REFIN_0")
    ole = document.querySelector("#id_oleCliente-0-OLE_0")
    bari = document.querySelector("#id_bariCliente-0-BARI_0")
    
    if(document.getElementById("id_nome_da_Empresa").value == "") {
        alert('Por favor, preencha o campo nome'); 
    }
    if (loasBrasil.checked == false && loasCidade.checked == false && bmg.checked == false && 
        siape.checked == false && refin.checked == false && ole.checked == false && bari.checked == false){
        alert("Por favor escolha sua proposta!")
    }
    if(document.getElementById("id_pacotesCliente-0-pacotes").value == ""){
        alert('Por favor, selecione seu pacote!'); 
    }
    
   
}   

   


