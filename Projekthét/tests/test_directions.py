

from marrakech.model.directions import Direction, RotationDirection


def test_rotate():
    # hozzunk létre egy irány objektumot
    d=Direction.RIGHT
    #forgassuk el
    result = d.rotate(RotationDirection.LEFT)
    #ellenőrizzük a forgatás eredményét
    assert result==Direction.UP

    d = Direction.RIGHT
    result = d.rotate(RotationDirection.RIGHT)
    assert result==Direction.DOWN

    d = Direction.LEFT
    result = d.rotate(RotationDirection.LEFT)
    assert result==Direction.DOWN
        
    d = Direction.LEFT
    result = d.rotate(RotationDirection.RIGHT)
    assert result==Direction.UP
       
    d = Direction.UP
    result = d.rotate(RotationDirection.LEFT)
    assert result==Direction.LEFT
       
    d = Direction.UP
    result = d.rotate(RotationDirection.RIGHT)
    assert result==Direction.RIGHT

    d = Direction.DOWN
    result = d.rotate(RotationDirection.LEFT)
    assert result==Direction.RIGHT
    
    d = Direction.DOWN
    result = d.rotate(RotationDirection.RIGHT)
    assert result==Direction.LEFT
