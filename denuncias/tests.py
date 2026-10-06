from django.test import TestCase

from denuncias.models import Usuario, Estado, Caso, Denuncia


class DenunciaModelTestCase(TestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.usuario = Usuario.objects.create_user(
            username='inspector1',
            email='inspector@siram.com',
            password='password123'
        )

        # Crear un estado inicial
        self.estado = Estado.objects.create(
            nombre='Pendiente'
        )

        # Crear un caso asociado
        self.caso = Caso.objects.create(
            estado=self.estado
        )

    def test_crear_denuncia(self):
        # Crear una denuncia
        denuncia = Denuncia.objects.create(
            fuente='Municipal',
            descripcion='Se constata animal atado sin agua.',
            estado=self.estado,
            caso=self.caso
        )

        # Verificar que se guardó correctamente
        self.assertEqual(denuncia.fuente, 'Municipal')
        self.assertEqual(denuncia.estado.nombre, 'Pendiente')
        self.assertEqual(denuncia.caso, self.caso)

        # Verificar que existe una denuncia
        self.assertEqual(Denuncia.objects.count(), 1)