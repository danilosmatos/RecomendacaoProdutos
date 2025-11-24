import time
from algorithms.productController import ProductController

def medir_performance_avl(controller, num_itens=5000):
    print(f"\nTeste de Performance da Inserção AVL ({num_itens} Categorias)---")
    
    arvore_teste = controller.arvore_categorias
    dados = [f"Categoria_{i:05d}" for i in range(num_itens)]
    
    inicio = time.time()
    for dado in dados:
        arvore_teste.raiz = arvore_teste._inserir_recursivo(arvore_teste.raiz, dado)
    fim = time.time()

    tempo = fim - inicio
    print(f"\nTempo total de inserção AVL para {num_itens} itens: {tempo:.4f} segundos.")
    print("Complexidade: O(log n)")
    
    return tempo

if __name__ == "__main__":
    app_controller = ProductController()
    medir_performance_avl(app_controller)